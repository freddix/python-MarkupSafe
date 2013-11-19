%define		module	MarkupSafe

Summary:	Implements a XML/HTML/XHTML Markup safe string for Python
Name:		python-%{module}
Version:	0.18
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/M/MarkupSafe/%{module}-%{version}.tar.gz
# Source0-md5:	f8d252fd05371e51dec2fe9a36890687
URL:		http://github.com/mitsuhiko/markupsafe
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements a XML/HTML/XHTML Markup safe string for Python.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%dir %{py_sitedir}/markupsafe
%attr(755,root,root) %{py_sitedir}/markupsafe/*.so
%{py_sitedir}/markupsafe/*.py[co]
%{py_sitedir}/*.egg-info

