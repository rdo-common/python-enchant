%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-enchant
Version:        1.1.3
Release:        2%{?dist}
Summary:        Python bindings for Enchant spellchecking library

Group:          Development/Languages
License:        LGPL
URL:            http://pyenchant.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/pyenchant/pyenchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel enchant-devel
Requires:   python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")

Provides:       PyEnchant

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


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
# First the architecture-independent files
%dir %{python_sitelib}/enchant
%dir %{python_sitelib}/enchant/checker
%dir %{python_sitelib}/enchant/tokenize
%{python_sitelib}/enchant/*.py
%{python_sitelib}/enchant/*.pyc
%ghost %{python_sitelib}/enchant/*.pyo
%{python_sitelib}/enchant/*/*.py
%{python_sitelib}/enchant/*/*.pyc
%ghost %{python_sitelib}/enchant/*/*.pyo
# Now the architecture-specific files
%dir %{python_sitearch}/enchant
%{python_sitearch}/enchant/_enchant.so


%changelog
* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-2
- Remove %%{enchant_dir} macro
- Add %%dir for architecture-specific directory
- Add "Provides:" for PyEnchant
- Remove "Requires:" on enchant (Brian Pepple)

* Mon Jan 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-1
- Initial packaging
