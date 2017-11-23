Summary:	Oxyd clone
Summary(pl.UTF-8):	Klon gry Oxyd
Name:		enigma
Version:	1.21
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/enigma-game/%{name}-%{version}.tar.gz
# Source0-md5:	d2f4a099a704fdf7f12d024d2b7e6d1b
Patch0:		%{name}-desktop.patch
Patch1:		0003-prevent-ImageMagick-inserting-timestamps-to-PNGs.patch
Patch2:		0004-src-lev-Proxy.cc-fix-check-for-basic_ifstream-s-read.patch
URL:		http://www.nongnu.org/enigma/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0.6
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xerces-c-devel >= 2.4
BuildRequires:	zlib-devel
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
Requires:	SDL_mixer >= 1.2.5
Requires:	SDL_ttf >= 2.0.6
Requires:	xerces-c >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enigma is a puzzle game inspired by Oxyd on the Atari ST and
Rock'n'Roll on the Amiga: You control a small black marble and have to
find and uncover all pairs of identical Oxyd stones in each landscape.
Sounds simple? It would be, if it weren't for hidden traps, vast
mazes, insurmountable obstacles and lots of hairy puzzles, blocking
your direct way to the Oxyd stones...

%description -l de.UTF-8
Bei Enigma handelt es sich um ein Remake des 1990 erschienen
Spiele-Klassikers Oxyd. Das Ziel des Spiels ist schnell erklärt:
Versuchen Sie alle gleichfarbigen "Oxyd"-Steine in jeder Landschaft zu
finden und aufzudecken. Hört sich einfach an? Wäre es vielleicht auch,
würden nicht versteckte Fallen, gewaltige Irrgärten, scheinbar
unüberwindliche Hindernisse und viele, viele Rätsel den direkten Weg
zu den Steinen blockieren...

%description -l pl.UTF-8
Enigma jest grą logiczną zainspirowaną przez Oxyd z Atari ST i
Rock'n'Roll z Amigi. Kontroluje się małą czarną kulkę mając za zadanie
odnaleźć i odkryć wszystkie pary identycznych kamieni Oxyd na każdej
planszy. Proste? Było by, gdyby nie ukryte pułapki, przepastne
labirynty, niepokonane przeszkody i mnóstwo włochatych zagadek
blokujących drogę do kamieni Oxyd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT{%{_libdir}/libenet.a,%{_includedir}/enet}

# generic license texts
%{__rm} $RPM_BUILD_ROOT%{_docdir}/enigma/{COPYING,gpl.txt,lgpl.txt}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/enigma
%{_datadir}/%{name}
%{_desktopdir}/enigma.desktop
%{_iconsdir}/hicolor/48x48/apps/enigma.png
%{_pixmapsdir}/enigma.png
%{_mandir}/man6/enigma.6*
%dir %{_docdir}/enigma
%{_docdir}/enigma/ACKNOWLEDGEMENTS
%{_docdir}/enigma/CHANGES
%{_docdir}/enigma/README
%{_docdir}/enigma/index.html
%{_docdir}/enigma/images
%dir %{_docdir}/enigma/manual
%{_docdir}/enigma/manual/enigma.html
%lang(de) %{_docdir}/enigma/manual/enigma_de.html
%lang(fr) %{_docdir}/enigma/manual/enigma_fr.html
%lang(ru) %{_docdir}/enigma/manual/enigma_ru.html
%{_docdir}/enigma/manual/images
%{_docdir}/enigma/reference
