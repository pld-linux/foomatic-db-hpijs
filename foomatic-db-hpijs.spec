%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic Data for the HPIJS Printer Drivers
Summary(pl):	Informacje foomatic dla sterownika drukarek HPIJS
Name:		foomatic-db-hpijs
Version:	1.3.1
Release:	20030303
Epoch:		1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}-%{release}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	foomatic-db-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foomatic Data for the HPIJS Printer Drivers.

%description -l pl
Informacje foomatic dla sterownika drukarek HPIJS.

%prep
%setup -q -n %{name}-%{version}-%{release}

%build
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
