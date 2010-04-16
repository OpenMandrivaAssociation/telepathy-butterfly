Name:           telepathy-butterfly
Version:        0.5.8
Release:        %mkrel 1
Summary:        MSN connection manager for Telepathy

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:	dbus-devel
BuildRequires:  python-devel
BuildRequires:	pkgconfig

Requires:	python-telepathy
Requires:	python-papyon
Requires:	dbus
Requires:	telepathy-filesystem


%description
An MSN connection manager that handles presence, personal messages,
and conversations

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_prefix}/lib/telepathy-butterfly
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{python_sitelib}/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
./configure --prefix=%_prefix --libexecdir=%_prefix/lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT
