#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Table
Summary:	Data::Table - Data type related to database tables, spreadsheets, etc.
Summary(pl):	Data::Table - Typ danych dotycz±cy tabel bazodanowych, arkuszy kalkulacyjnych itp.
Name:		perl-Data-Table
Version:	1.34
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.geocities.com/easydatabase/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
