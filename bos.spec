%define	name	bos
%define	version 2.4
%define rel	2
%define	release	%mkrel %rel
%define	Summary	Invasion: Battle of survival

Name:		%{name} 
Summary:	A real time strategy game
Version:	%{version} 
Release:	%{release} 
Source0:	boswars-%{version}-src.tar.gz
# It doesn't provide it's own icon yet
# Found this on their patch tracker
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
URL:		http://bos.seul.org/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	scons X11-devel lua-devel mesagl-devel libogg-devel
BuildRequires:	SDL-devel bzip2-devel oggvorbis-devel libmikmod-devel
BuildRequires:	libpng-devel libmng-devel
BuildRequires:  MesaGLU-devel ImageMagick libtheora-devel

%description
Invasion - Battle of Survival is a real-time strategy game using
the Stratagus game engine. 

%prep
%setup -q -n boswars-%{version}-src

%build
scons opengl=1 
cp boswars{,-gl}
scons -c .
scons -c build export
scons opengl=0

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_gamesbindir,%_gamesdatadir/bos}
install -m755 boswars $RPM_BUILD_ROOT%_gamesbindir
install -m755 boswars-gl $RPM_BUILD_ROOT%_gamesbindir

cp -ra campaigns graphics languages maps scripts sounds units video $RPM_BUILD_ROOT%{_gamesdatadir}/bos/
cat << EOF > ./bos-gl
#!/bin/sh
boswars-gl \$@ -d %{_gamesdatadir}/bos/
EOF
cat << EOF > ./bos.sh
#!/bin/sh
boswars \$@ -d %{_gamesdatadir}/bos/
EOF
install -m755 ./bos.sh -D $RPM_BUILD_ROOT%{_gamesbindir}/bos
install -m755 ./bos-gl -D $RPM_BUILD_ROOT%{_gamesbindir}/bos-gl

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{Summary}
Comment=%{Summary} - a real time strategy game
Exec=%{_gamesbindir}/bos
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;X-MandrivaLinux-MoreApplications-Games-Strategy;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-gl.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{Summary} (OpenGL)
Comment=%{Summary} - a real time strategy game
Exec=%{_gamesbindir}/bos-gl
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;X-MandrivaLinux-MoreApplications-Games-Strategy;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%update_menus

%files 
%defattr(-,root,root)
%doc doc/*
%dir %{_gamesdatadir}/bos/
%{_gamesdatadir}/bos/*
%{_gamesbindir}/bos
%{_gamesbindir}/bos-gl
%{_gamesbindir}/boswars
%{_gamesbindir}/boswars-gl
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/mandriva-%{name}-gl.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


