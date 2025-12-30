%global module fabulous

Summary:	Makes your terminal output totally fabulous
Name:		python-fabulous
Version:	0.4.0
Release:	3
License:	Apache 2.0 / OFL
Group:		Development/Python
URL:		https://pypi.org/project/fabulous/
Source0:	https://pypi.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Makes your terminal output totally fabulous

%files
%{_bindir}/%{module}-*
%{py_sitedir}/fabulous
%{py_sitedir}/fabulous-*.*-info

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n fabulous-%{version}

%build
%py_build

%install
%py_install

