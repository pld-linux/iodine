#
# Conditional build:
%bcond_without	selinux	# SELinux support
%bcond_without	systemd	# systemd support
#
Summary:	IP over DNS is now easy
Summary(pl.UTF-8):	Łatwa w użyciu implementacja IP over DNS
Name:		iodine
Version:	0.7.0
Release:	3
License:	MIT
Group:		Networking
Source0:	http://code.kryo.se/iodine/%{name}-%{version}.tar.gz
# Source0-md5:	fdbf3b81cd69caf5230d76a8b039fd99
Patch0:		%{name}-opt.patch
Patch1:		%{name}-make.patch
Patch2:		libsystemd.patch
URL:		http://code.kryo.se/iodine/
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a piece of software that lets you tunnel IPv4 data through a
DNS server. This can be usable in different situations where Internet
access is firewalled, but DNS queries are allowed.

%description -l pl.UTF-8
Ten pakiet pozwala tunelować dane IPv4 poprzez serwer DNS. Może to być
przydatne w różnych sytuacjach kiedy dostęp do Internetu jest
ograniczony firewallem, ale dozwolone są zapytania DNS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -D_GNU_SOURCE %{?with_selinux:-DHAVE_SETCON} %{?with_systemd:-DHAVE_SYSTEMD}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/iodine
%attr(755,root,root) %{_sbindir}/iodined
%{_mandir}/man8/iodine.8*
