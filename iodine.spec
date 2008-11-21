Summary:	IP over DNS is now easy
Summary(pl.UTF-8):	Łatwa w użyciu implementacja IP over DNS
Name:		iodine
Version:	0.4.0
Release:	1
License:	ISC
Group:		Networking
Source0:	http://code.kryo.se/iodine/%{name}-%{version}.tar.gz
# Source0-md5:	82d331f75a99d1547e0ccc3c3efd0a7a
Patch0:		%{name}-opt.patch
Patch1:		%{name}-make.patch
URL:		http://code.kryo.se/iodine/
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

%build
%{__make} -C src \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/iodine
%attr(755,root,root) %{_sbindir}/iodined
%{_mandir}/man8/iodine.8*
