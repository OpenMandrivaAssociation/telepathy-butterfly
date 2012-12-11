Name:           telepathy-butterfly
Version:        0.5.15
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
Requires:	python-papyon >= 0.4.9
Requires:	dbus
Requires:	telepathy-filesystem
Suggests:	python-libproxy


%description
An MSN connection manager that handles presence, personal messages,
and conversations

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_prefix}/lib/telepathy-butterfly
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{python_sitelib}/butterfly

#--------------------------------------------------------------------

%prep
%setup -q

%build
./configure --prefix=%_prefix --libexecdir=%_prefix/lib
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%changelog
* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.5.15-1mdv2011.0
+ Revision: 633984
- update to new version 0.5.15

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.5.14-2mdv2011.0
+ Revision: 592165
- rebuild for python 2.7

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 0.5.14-1mdv2011.0
+ Revision: 582220
- update to new version 0.5.14

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.12-1mdv2011.0
+ Revision: 567232
- update to 0.5.12
- improve package dir ownership

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 0.5.11-1mdv2010.1
+ Revision: 548354
- Release 0.5.11

* Sun Apr 25 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.9-1mdv2010.1
+ Revision: 538540
- Update to new version 0.5.9
- Suggest new optional dependency python-libproxy for automatic
  retrieval of proxy settings

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.8-1mdv2010.1
+ Revision: 535570
- update to new version 0.5.8

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 0.5.6-1mdv2010.1
+ Revision: 518687
- new version 0.5.6

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 494176
- update to new version 0.5.4

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 462142
- update to new version 0.5.3

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 0.5.2-1mdv2010.0
+ Revision: 458738
- Release 0.5.2

* Mon Sep 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 440818
- update to new version 0.5.1

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 402831
- Update to new version 0.5.0
- Requires papyon instead of pymsn now

* Tue Jun 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.4-1mdv2010.0
+ Revision: 386454
- update to new version 0.3.4

* Sat Jan 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.3-1mdv2009.1
+ Revision: 327961
- update to new version 0.3.3

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.3.2-4mdv2009.1
+ Revision: 320648
- rebuild for new python

* Fri Aug 22 2008 Götz Waschk <waschk@mandriva.org> 0.3.2-3mdv2009.0
+ Revision: 275075
- move to Mandriva standard for libexecdir

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 261460
- rebuild

* Wed Jul 30 2008 Frederik Himpe <fhimpe@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 254928
- New upstream version 0.3.2
- remove DESTDIR patch, it's not needed anymore and so we can use
  %%makeinstall_std now
- Fix license

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2009.0
+ Revision: 254357
- rebuild

* Thu Mar 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.1-1mdv2008.1
+ Revision: 180500
- New version 0.3.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 10 2007 Michael Scherer <misc@mandriva.org> 0.1.4-1mdv2008.0
+ Revision: 37793
- update to 0.1.4


* Sat Jan 13 2007 Michael Scherer <misc@mandriva.org> 0.1.2-5mdv2007.0
+ Revision: 108361
- use %%rel for mkrel
- fix Requires

* Fri Dec 15 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.2-4mdv2007.1
+ Revision: 97480
- Rebuild against new python
- Rebuild against new python

* Fri Oct 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.2-2mdv2007.1
+ Revision: 63785
- Fix BuildRequires
- Import telepathy-butterfly

