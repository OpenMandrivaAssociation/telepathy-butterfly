%define rel 5

Name:           telepathy-butterfly
Version:        0.1.2
Release:        %mkrel %rel
Summary:        MSN connection manager for Telepathy

Group:          Networking/Instant messaging
License:        GPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:	dbus-devel
BuildRequires:  python-devel
BuildRequires:	pkgconfig

Requires:	python-telepathy
Requires:	python-pymsn
Requires:	dbus
Requires:	telepathy-filesystem


%description
An MSN connection manager that handles presence, personal messages,
and conversations


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{python_sitelib}/*


