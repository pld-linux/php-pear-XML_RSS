%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	XML_RSS
Summary:	%{_pearname} - RSS parser
Summary(pl.UTF-8):	%{_pearname} - parser RSS
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0d5419af419cda4afafab7bce3a68168
URL:		http://pear.php.net/package/XML_RSS/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-XML_Parser > 1.0.1
Requires:	php-pear-XML_Tree
Obsoletes:	php-pear-XML_RSS-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Parser do dokumentów w formacie RSS (RDF Site Summary, gdzie RDF jest
skrótem od Resource Description Framework).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/*.php
