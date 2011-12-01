%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define packagename AddOns

Name:           python-peak-util-addons
Version:        0.6
Release:        4.1%{?dist}
Summary:        Dynamically extend other objects with AddOns

Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://pypi.python.org/pypi/AddOns
Source0:        http://pypi.python.org/packages/source/A/%{packagename}/%{packagename}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

Requires:       python-decoratortools >= 1.5

%description
In any sufficiently-sized application or framework, it's common to end up
lumping a lot of different concerns into the same class.  For example, you may
have business logic, persistence code, and UI all jammed into a single class.
Attribute and method names for all sorts of different operations get shoved
into a single namespace -- even when using mixin classes.

Separating concerns into different objects, however, makes it easier to write
reusable and separately-testable components.  The AddOns package
(``peak.util.addons``) lets you manage concerns using ``AddOn`` classes.

%prep
%setup -q -n %{packagename}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6-2
- Rebuild for Python 2.6

* Sun Aug 12 2008 Luke Macken <lmacken@redhat.com> - 0.6-1
- Initial package for Fedora
