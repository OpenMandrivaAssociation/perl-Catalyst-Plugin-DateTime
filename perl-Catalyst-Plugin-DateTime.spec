%define upstream_name	Catalyst-Plugin-DateTime
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	DateTime plugin for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 2.990.0
BuildRequires:	perl(DateTime) >= 0.200.0

BuildArch:	noarch

%description
This module's intention is to make the wonders of DateTime easily
accesible within a Catalyst application via the Catalyst::Plugin
interface.

It adds the methods datetime and dt to the Catalyst namespace.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
## scottk ##
## Temporarily disabled test due to error:
## "Cannot determine local time zone"
## when built in lbd automated build environment
##-__make test

%install
%makeinstall_std

%files 
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 680731
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 505419
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2010.0
+ Revision: 430270
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.03-4mdv2008.1
+ Revision: 136677
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-4mdv2008.0
+ Revision: 86004
- rebuild


* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 0.03-3mdv2007.0
- Disabled testing due to failure in automated build enviornment

* Fri Jun 16 2006 Scott Karns <scottk@mandriva.org> 0.03-2mdv2007.0
- Updated spec to comply with Mandriva perl packaging policies

* Sun Jan 22 2006 Scott Karns <scott@karnstech.com> 0.03-1mdk
- Initial Mdv release

