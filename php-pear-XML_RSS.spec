%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RSS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - RSS parser
Summary(pl):	%{_pearname} - parser RSS
Name:		php-pear-%{_pearname}
Version:	0.9.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	08651112f90df52f7dd4af70cd058f1e
URL:		http://pear.php.net/package/XML_RSS/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

In PEAR status of this package is: %{_status}.

%description -l pl
Parser do dokumentów w formacie RSS (RDF Site Summary, gdzie RDF jest
skrótem od Resource Description Framework).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/%{_class}/*.php
