Name:           telepathy-butterfly
Version:        0.3.1
Release:        %mkrel 1
Summary:        MSN connection manager for Telepathy

Group:          Networking/Instant messaging
License:        GPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		telepathy-butterfly-0.3.1-fix-destdir.patch
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

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_prefix}/libexec/telepathy-butterfly
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{python_sitelib}/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT
