Summary: Mem/Swap monitoring dockapp for WindowMaker
Name:		wmmemmon
Version: 1.0.1
Release: %mkrel 2
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.bz2
URL:		http://www.sh.rim.or.jp/~ssato/wmmemmon-e.html
BuildRequires:	XFree86-devel, xpm-devel, ImageMagick
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Mem/Swap monitoring dockapp for WindowMaker. Outside circle is Mem usage
in percent, inside is swap. It works fine with AfterStep and BlackBox.

%prep

%setup

%build
%configure
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

install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="%{name}.png"\\
                 needs="wmaker" section="Applications/Monitoring" title="WmMemMon"\\
                 longtitle="Mem/Swap monitoring dockapp for WindowMaker"
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README THANKS ChangeLog TODO
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%{_mandir}/man1/*

