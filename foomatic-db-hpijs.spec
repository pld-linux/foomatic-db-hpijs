%define		ver 1.3.1
%define		rel 4
%include	/usr/lib/rpm/macros.perl
Summary:	Foomatic Data for the HPIJS Printer Drivers
Summary(pl):	Informacje foomatic dla sterownika drukarek HPIJS
Name:		foomatic-db-hpijs
Version:	%{ver}.%{rel}
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{ver}-%{rel}.tar.gz
# Source0-md5:	23a5a96ac71eb703a59d6e8ab0c22de2
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	foomatic-db-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foomatic Data for the HPIJS Printer Drivers.

%description -l pl
Informacje foomatic dla sterownika drukarek HPIJS.

%prep
%setup -q -n %{name}-%{ver}-%{rel}

%build
%{__aclocal}
%{__autoconf}
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
%doc ChangeLog TODO README USAGE
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
