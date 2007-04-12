%define module	Catalyst-Plugin-DateTime
%define name	perl-%{module}
%define	modprefix Catalyst

%define version 0.03

%define	rel	3
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DateTime plugin for Catalyst
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(DateTime) >= 0.20
Buildarch:	noarch

%description
This module's intention is to make the wonders of DateTime easily
accesible within a Catalyst application via the Catalyst::Plugin
interface.

It adds the methods datetime and dt to the Catalyst namespace.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%__make

%check
## scottk ##
## Temporarily disabled test due to error:
## "Cannot determine local time zone"
## when built in lbd automated build environment
##-__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

