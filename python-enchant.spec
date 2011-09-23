Name:           python-enchant
Version:        1.6.5
Release:        2%{?dist}
Summary:        Python bindings for Enchant spellchecking library

Group:          Development/Languages
License:        LGPLv2+
URL:            http://pyenchant.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/pyenchant/pyenchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel enchant-devel
BuildRequires:  python-setuptools >= 0:0.6a9
# Work around a problem with libenchant versioning
# (python-enchant-1.3.1 failed to work with enchant-1.4.2-2.fc10)
Requires:       enchant >= 1.5.0

# Package was arch specific before
Obsoletes:      python-enchant < 1.6.5

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
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --single-version-externally-managed
rm -rf $RPM_BUILD_ROOT/%{python_sitelib}/*.egg-info
# Directories used in windows build
rm -rf $RPM_BUILD_ROOT/%{python_sitelib}/enchant/lib
rm -rf $RPM_BUILD_ROOT/%{python_sitelib}/enchant/share


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt TODO.txt
%dir %{python_sitelib}/enchant
%dir %{python_sitelib}/enchant/checker
%dir %{python_sitelib}/enchant/tokenize
%{python_sitelib}/enchant/*.py
%{python_sitelib}/enchant/*.py[co]
%{python_sitelib}/enchant/*/*.py
%{python_sitelib}/enchant/*/*.py[co]


%changelog
* Fri Sep 23 2011 Radek Novacek <rnovacek@redhat.com> 1.6.5-2
- Obsolete old arch-specific version

* Fri Sep 23 2011 Radek Novacek <rnovacek@redhat.com> 1.6.5-1
- Update to version 1.6.5
- Change architecture to noarch
- Change python_sitearch to python_sitelib
- Changelog in no longer in source tarball
- Remove nonpacked files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Feb  1 2010 Stepan Kasal <skasal@redhat.com> - 1.3.1-6
- add a require to work around a problem with libenchant versioning

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.1-3
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.1-2
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.1-1
- Update to 1.3.1
- Change license tag to LGPLv2+

* Sat Jan 13 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.0-1
- Update to 1.3.0
- Add ChangeLog and TODO.txt as documentation

* Sat Dec 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.2.0-2
- Rebuild for Python 2.5

* Tue Nov  7 2006 José Matos <jamatos[AT]fc.up.pt> - 1.2.0-1
- New upstream release

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.1.5-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 José Matos <jamatos[AT]fc.up.pt> - 1.1.5-4
- Rebuild for FC-6.
- Unghost .pyo files.

* Tue Feb 14 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.5-3
- Rebuild for Fedora Extras 5

* Tue Feb 07 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.5-2
- Rebuild

* Sat Feb 04 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.5-1
- Update to 1.1.5

* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-3
- Use %%{python_sitearch} instead of %%{python_sitelib} (for x86_64)

* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-2
- Remove %%{enchant_dir} macro
- Add %%dir for architecture-specific directory
- Add "Provides:" for PyEnchant
- Remove "Requires:" on enchant (Brian Pepple)

* Mon Jan 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.1.3-1
- Initial packaging
