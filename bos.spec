%define	name	bos
%define	version 2.6.1
%define rel	2
%define	release	%rel
%define	Summary	Invasion: Battle of survival

Name:		%{name} 
Summary:		A real time strategy game
Version:		%{version} 
Release:		%{release} 
Source0:		http://www.boswars.org/dist/releases/boswars-%{version}-src.zip
# It doesn't provide it's own icon yet
# Found this on their patch tracker
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
Patch:		boswars-2.6.1-scons-blows.patch
URL:		http://www.boswars.org/
Group:		Games/Strategy
License:	GPLv2+
BuildRequires:	scons
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gl)
%description
Invasion - Battle of Survival is a real-time strategy game using
the Stratagus game engine. 

%prep
%setup -q -n boswars-%{version}-src
%patch -p0 


%build
%setup_compile_flags
scons opengl=1

%install
mkdir -p %{buildroot}{%_gamesbindir,%_gamesdatadir/bos}
install -m755 boswars %{buildroot}%_gamesbindir

cp -ra campaigns graphics intro languages maps scripts sounds units %{buildroot}%{_gamesdatadir}/bos/
cat << EOF > ./bos.sh
#!/bin/sh
boswars \$@ -d %{_gamesdatadir}/bos/
EOF
install -m755 ./bos.sh -D %{buildroot}%{_gamesbindir}/bos

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bos Wars
Comment=Invasion: Battle of survival - a real time strategy game
Exec=%{_gamesbindir}/bos
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;
EOF

%files 
%doc doc/*
%dir %{_gamesdatadir}/bos/
%{_gamesdatadir}/bos/*
%{_gamesbindir}/bos
%{_gamesbindir}/boswars
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Wed Jan 05 2011 Funda Wang <fwang@mandriva.org> 2.6.1-2mdv2011.0
+ Revision: 628663
- tighten BR

* Wed Sep 22 2010 Zombie Ryushu <ryushu@mandriva.org> 2.6.1-1mdv2011.0
+ Revision: 580518
- Upgrade to 2.6.1
- Upgrade to 2.6.1
- Upgrade to 2.6.1

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 2.5-3mdv2010.1
+ Revision: 528528
- more gcc patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-2mdv2009.1
+ Revision: 358043
- rebuild

* Wed Mar 11 2009 Emmanuel Andry <eandry@mandriva.org> 2.5-1mdv2009.1
+ Revision: 353563
- New version 2.5
- fix gcc43 build with gentoo patch

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.4.1-2mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 2.4.1-2mdv2008.0
+ Revision: 80030
- only one build (GL is a run time option)

  + Funda Wang <fwang@mandriva.org>
    - fix URL

* Wed Sep 05 2007 Funda Wang <fwang@mandriva.org> 2.4.1-1mdv2008.0
+ Revision: 79688
- New version 2.4.1

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Aug 27 2007 Thierry Vignaud <tv@mandriva.org> 2.4-2mdv2008.0
+ Revision: 71993
- add a non GL build since the GL version makes a radeon 8500 slow like hell for no rendering improvement
- drop debian style menu entry

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 2.4-1mdv2008.0
+ Revision: 64185
- new release (that now build with lua-5.1)
- fix versionning

* Mon Jul 02 2007 Olivier Blin <oblin@mandriva.com> 2.3-1mdv2008.0
+ Revision: 47151
- build in %%build section...

  + Thierry Vignaud <tv@mandriva.org>
    - new release
    - drop noarch tag, add buildrequires (stratagus engine was merged)
    - new release
    - drop noarch tag, add buildrequires (stratagus engine was merged)


* Wed Jan 17 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.1-1mdv2007.0
+ Revision: 109769
- new release: 2.0.1

* Wed Dec 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0-1mdv2007.1
+ Revision: 96327
- Convert icons upfront to avoid dependency on ImageMagick and related weirdness
- 2.0
  add xdg menu
- Import bos

* Fri Aug 19 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1-3mdk
- fix buildrequires
- fix hidden-file-or-dir

* Sat Jul 09 2005 Eskild Hustvedt <eskild@mandrake.org> 1.1-2mdk
- Provide it's own icon
- Launchscript accepts commandline parameters

* Sat Jul 09 2005 Eskild Hustvedt <eskild@mandrake.org> 1.1-1mdk
- Initial Mandriva Linux package

