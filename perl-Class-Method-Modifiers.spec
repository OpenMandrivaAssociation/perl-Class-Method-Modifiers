%define upstream_name    Class-Method-Modifiers
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Provides Moose-like method modifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/Class-Method-Modifiers-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildArch:	noarch

%description
Method modifiers are a powerful feature from the CLOS (Common Lisp Object
System) world.

In its most basic form, a method modifier is just a method that calls
'$self->SUPER::foo(@_)'. I for one have trouble remembering that exact
invocation, so my classes seldom re-dispatch to their base classes. Very
bad!

'Class::Method::Modifiers' provides three modifiers: 'before', 'around',
and 'after'. 'before' and 'after' are run just before and after the method
they modify, but can not really affect that original method. 'around' is
run in place of the original method, with a hook to easily call that
original method. See the 'MODIFIERS' section for more details on how the
particular modifiers work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Class


%changelog
* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 643366
- update to new version 1.07

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 601861
- update to new version 1.06

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 461264
- update to 1.05

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 403014
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2010.0
+ Revision: 387001
- update to new version 1.04

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2010.0
+ Revision: 383474
- update to new version 1.02

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 242072
- import perl-Class-Method-Modifiers


* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
- initial mdv release, generated with cpan2dist





