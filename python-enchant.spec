%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-enchant
Version:        1.1.3
Release:        1%{?dist}
Summary:        Python bindings for Enchant spellchecking library

Group:          Development/Languages
License:        LGPL
URL:            http://pyenchant.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/pyenchant/pyenchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel enchant-devel
Requires:   python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")
Requires:       enchant

%description
PyEnchant is a spellchecking library for Python, based on the Enchant
library by Dom Lachowicz.


%prep
%setup -q -n pyenchant-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%define enchant_dir %{python_sitearch}/enchant

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%dir %{enchant_dir}
%dir %{enchant_dir}/checker
%dir %{enchant_dir}/tokenize
%{enchant_dir}/*.py
%{enchant_dir}/*.pyc
%ghost %{enchant_dir}/*.pyo
%{enchant_dir}/*/*.py
%{enchant_dir}/*/*.pyc
%ghost %{enchant_dir}/*/*.pyo
%{enchant_dir}/_enchant.so

%changelog
* Mon Jan 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-1
- Initial packaging
