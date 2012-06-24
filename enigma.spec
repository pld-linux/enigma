Summary:	Oxyd clone
Summary(pl):	Klon gry Oxyd
Name:		enigma
Version:	0.60
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/enigma/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua40-devel >= 4.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
URL:		http://www.freesoftware.fsf.org/enigma/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Enigma is a puzzle game inspired by Oxyd on the Atari ST and
Rock'n'Roll on the Amiga: You control a small black marble and have to
find and uncover all pairs of identical Oxyd stones in each landscape.
Sounds simple? It would be, if it weren't for hidden traps, vast
mazes, insurmountable obstacles and lots of hairy puzzles, blocking
your direct way to the Oxyd stones...

%description -l pl
Enigma jest gr� logiczn� zainspirowan� przez Oxyd z Atari ST i
Rock'n'Roll z Amigi. Kontroluje si� ma�� czarn� kulk� maj�c za zadanie
odnale�� i odkry� wszystkie pary identycznych kamieni Oxyd na ka�dej
planszy. Proste? By�o by, gdyby nie ukryte pu�apki, przepastne
labirynty, niepokonane przeszkody i mn�stwo w�ochatych zagadek
blokuj�cych drog� do kamieni Oxyd.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/enigma/{fonts,sound,gfx,levels},%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_applnkdir}/Games}

install enigma.6		$RPM_BUILD_ROOT%{_mandir}/man6
install enigma			$RPM_BUILD_ROOT%{_bindir}
install fonts/*.{png,txt,bmf}	$RPM_BUILD_ROOT%{_datadir}/enigma/fonts
install gfx/*.png		$RPM_BUILD_ROOT%{_datadir}/enigma/gfx
install levels/*.{lua,png,txt}	$RPM_BUILD_ROOT%{_datadir}/enigma/levels
install sound/*.{wav,s3m}	$RPM_BUILD_ROOT%{_datadir}/enigma/sound
install *.lua			$RPM_BUILD_ROOT%{_datadir}/enigma

install %{SOURCE1}		$RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2}		$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO CREATING-LEVELS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/enigma
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
