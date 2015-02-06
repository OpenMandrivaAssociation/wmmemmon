Summary: Mem/Swap monitoring dockapp for WindowMaker
Name:		wmmemmon
Version: 1.0.1
Release: 9
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.bz2
URL:		http://www.sh.rim.or.jp/~ssato/wmmemmon-e.html
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	imagemagick

%description
Mem/Swap monitoring dockapp for WindowMaker. Outside circle is Mem usage
in percent, inside is swap. It works fine with AfterStep and BlackBox.

%prep
%setup

%build
%configure2_5x
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%_bindir
install -m 755 src/%name %buildroot%_bindir

install -m 755 -d %buildroot%_mandir/man1
install -m 755 doc/%name.1 %buildroot%_mandir/man1/

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
convert icons/%{name}-16x16.xpm %buildroot%{_miconsdir}/%{name}.png
convert icons/%{name}-32x32.xpm %buildroot%{_iconsdir}/%{name}.png
convert icons/%{name}-48x48.xpm %buildroot%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}                 
Categories=System;Monitor;
Name=WmMemMon                 
Comment=Mem/Swap monitoring dockapp for WindowMaker
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README THANKS ChangeLog TODO
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.0.1-7mdv2011.0
+ Revision: 634819
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2010.0
+ Revision: 434887
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2009.0
+ Revision: 262058
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 256203
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2008.1
+ Revision: 135531
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import wmmemmon


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-2mdk
- Rebuild

* Tue May  4 2004 Michael Scherer <misc@mandrake.org> 1.0.1-1mdk
- New release 1.0.1
- use macro
- remove Prefix, and Requires

* Thu Apr 10 2003 HA Quôc-Viêt <viet@mandrakesoft.com> 1.0.0-1mdk
- New release.
- xpm icons converted to png at compile time from the spec.

* Wed Mar 27 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.7.0-1mdk
- New release.
- xpm icons converted to png.
- menu file has "needs=wmaker" instead of "needs=x11".
- did install (binary and manpage) by hand due to new naming convention.

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.6.0-1mdk
- New release.
- and revamped website :o)
- xpm icons converted to png (new policy, oh well).

* Mon Oct 1 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.5.2-1mdk
- New release, no more libdockapp dependancy (integrated)
- now you can specify your own backlight color, I like rgb:50/B0/FF :o)

* Wed Jul 25 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.3.1-1mdk
- New release, with icons integrated :o)

* Tue Jun 19 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.2.0-2mdk
- Added icons from the author Seiichi SATO <sato@cvs-net.co.jp>

* Fri Jun 01 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.2.0-1mdk
- Initial release.

* Mon May 07 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.1.0-0mdk
- Initial packaging.
