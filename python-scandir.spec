# Created by pyp2rpm-3.3.2
%global pypi_name scandir

Name:           python-%{pypi_name}
Version:        1.10.0
Release:        1
Summary:        scandir, a better directory iterator and faster os
Group:          Development/Python
License:        New BSD License
URL:            https://github.com/benhoyt/scandir
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)

%description
scandir, a better directory iterator and faster os.walk() scandir() is a
directory iteration function like os.listdir(),

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%check
%{__python} setup.py test

%files
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/__pycache__/*
%{python_sitearch}/%{pypi_name}.py
%{python_sitearch}/_%{pypi_name}*.so
%{python_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
