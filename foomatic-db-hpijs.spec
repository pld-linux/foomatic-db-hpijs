%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic Data for the HPIJS Printer Drivers
Summary(pl.UTF-8):	Informacje foomatic dla sterownika drukarek HPIJS
Name:		foomatic-db-hpijs
Version:	20070919
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	63d0f32ef453f54bbe404bdf565116b1
URL:		http://www.linuxprinting.org/foomatic.html
Requires:	foomatic-db-engine >= 3.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foomatic Data for the HPIJS Printer Drivers.

%description -l pl.UTF-8
Informacje foomatic dla sterownika drukarek HPIJS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README USAGE
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
