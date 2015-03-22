#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooX
%define		pnam	HandlesVia
%include	/usr/lib/rpm/macros.perl
Summary:	MooX::HandlesVia - NativeTrait-like behavior for Moo
Name:		perl-MooX-HandlesVia
Version:	0.001007
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9744cfe9e431c6510d73409a27522e47
URL:		http://search.cpan.org/dist/MooX-HandlesVia/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Perl) >= 0.002006
BuildRequires:	perl(MooX::Types::MooseLike::Base) >= 0.23
BuildRequires:	perl-Class-Method-Modifiers
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Moo >= 1.003000
BuildRequires:	perl-Role-Tiny
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Fatal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooX::HandlesVia is an extension of Moo's 'handles' attribute
functionality. It provides a means of proxying functionality from an
external class to the given atttribute. This is most commonly used as
a way to emulate 'Native Trait' behavior that has become commonplace
in Moose code, for which there was no Moo alternative.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/MooX/HandlesVia.pm
%dir %{perl_vendorlib}/Data/Perl/Bool
%{perl_vendorlib}/Data/Perl/Bool/MooseLike.pm
%dir %{perl_vendorlib}/Data/Perl/Collection
%dir %{perl_vendorlib}/Data/Perl/Collection/Array
%{perl_vendorlib}/Data/Perl/Collection/Array/MooseLike.pm
%dir %{perl_vendorlib}/Data/Perl/Collection/Hash
%{perl_vendorlib}/Data/Perl/Collection/Hash/MooseLike.pm
%dir %{perl_vendorlib}/Data/Perl/Number
%{perl_vendorlib}/Data/Perl/Number/MooseLike.pm
%dir %{perl_vendorlib}/Data/Perl/String
%{perl_vendorlib}/Data/Perl/String/MooseLike.pm
%{_mandir}/man3/*
