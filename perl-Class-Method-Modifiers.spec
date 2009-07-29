%define upstream_name    Class-Method-Modifiers
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    provides Moose-like method modifiers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Class
