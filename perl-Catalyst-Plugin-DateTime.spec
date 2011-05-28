%define upstream_name	Catalyst-Plugin-DateTime
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	DateTime plugin for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 2.990.0
BuildRequires:	perl(DateTime) >= 0.200.0

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module's intention is to make the wonders of DateTime easily
accesible within a Catalyst application via the Catalyst::Plugin
interface.

It adds the methods datetime and dt to the Catalyst namespace.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

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
%{perl_vendorlib}/Catalyst
