%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       RSS
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - RSS parser
Summary(pl):	%{_class}_%{_subclass} - parser RSS
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

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
