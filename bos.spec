%define	name	bos
%define	version 2.3
%define rel	1
%define	release	%mkrel %rel
%define	Summary	Invasion: Battle of survival

Name:		%{name} 
Summary:	A real time strategy game
Version:	%{version} 
Release:	%{release} 
Source0:	boswars-2.3-src.tar.gz
# It doesn't provide it's own icon yet
# Found this on their patch tracker
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
URL:		http://bos.seul.org/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	scons X11-devel lua5.0-devel mesagl-devel libogg-devel
BuildRequires:	SDL-devel bzip2-devel oggvorbis-devel libmikmod-devel
BuildRequires:	libpng-devel libmng-devel
BuildRequires:  MesaGLU-devel ImageMagick libtheora-devel

%description
Invasion - Battle of Survival is a real-time strategy game using
the Stratagus game engine. 

%prep
%setup -q -n boswars-2.3-src

%build
scons opengl=1 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_gamesbindir,%_gamesdatadir/bos}
install -m755 boswars $RPM_BUILD_ROOT%_gamesbindir

cp -ra campaigns graphics languages maps scripts sounds units video $RPM_BUILD_ROOT%{_gamesdatadir}/bos/
cat << EOF > ./bos.sh
#!/bin/sh
boswars \$@ -d %{_gamesdatadir}/bos/
EOF
install -m755 ./bos.sh -D $RPM_BUILD_ROOT%{_gamesbindir}/bos

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

# Create a menu item
mkdir -p %{buildroot}%{_menudir}
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%name):command="%{_gamesbindir}/bos"\
 icon="%{name}.png" needs="X11" section="More Applications/Games/Strategy"\
 title="%{Summary}" longtitle="%{Summary} - a real time strategy game" \
 xdg="true"
EOF

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
%{_gamesbindir}/boswars
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


