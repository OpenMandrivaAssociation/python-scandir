# Created by pyp2rpm-3.3.2
%global pypi_name scandir

Name:           python-%{pypi_name}
Version:        1.10.0
Release:        %mkrel 2
Summary:        scandir, a better directory iterator and faster os
Group:          Development/Python
License:        New BSD License
URL:            https://github.com/benhoyt/scandir
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
scandir, a better directory iterator and faster os.walk() scandir() is a
directory iteration function like os.listdir(),

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
scandir, a better directory iterator and faster os.walk() scandir() is a
directory iteration function like os.listdir(),

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/%{pypi_name}.py
%{python3_sitearch}/_%{pypi_name}*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
