#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Table
Summary:	Data::Table - data type related to database tables, spreadsheets, etc
Summary(pl):	Data::Table - typ danych dotycz±cy tabel bazodanowych, arkuszy kalkulacyjnych itp.
Name:		perl-Data-Table
Version:	1.47
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40087b9c0945df52d78da475efe8ace3
URL:		http://www.geocities.com/easydatabase/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This perl package uses perl5 objects to make it easy for manipulating
spreadsheet data among disk files, database, and Web publishing.

A table object contains a header and a two-dimensional array of
scalars. Three class methods allow users to create a table object from
a CSV/TSV file or a database SQL selection in a snap.

Table methods provide basic access, add, delete row(s) or column(s)
operations, as well as more advanced sub-table extraction, table
sorting, record matching via keywords or patterns, table merging, and
web publishing.

%description -l pl
Ten pakiet perlowy u¿ywa obiektów Perla 5, aby u³atwiæ manipulowanie
danymi arkuszy kalkulacyjnych w plikach na dysku, bazach danych i
publikacjach WWW.

Obiekt tabeli zawiera nag³ówek i dwuwymiarow± tablicê skalarów. Trzy
metody klasy pozwalaj± u¿ytkownikom tworzyæ obiekt tabeli z pliku
CSV/TSV lub wyniku zapytania z bazy danych SQL.

Metody tabeli umo¿liwiaj± podstawowe operacje dostêpu, dodawania i
usuwania wierszy i kolumn, nieco bardziej zaawansowane wyci±ganie
podtabel, sortowanie tabel, dopasowywanie rekordów po s³owach
kluczowych lub wzorcach, ³±czenie tabel oraz publikowanie na WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# empty autosplit.ix
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/auto/Data/Table/autosplit.ix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
