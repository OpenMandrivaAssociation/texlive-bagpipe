Name:		texlive-bagpipe
Version:	34393
Release:	1
Summary:	Support for typesetting bagpipe music
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bagpipe
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typesetting bagpipe music in MusixTeX is needlessly tedious.
This package provides specialized and re-defined macros to
simplify this task.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/bagpipe
%doc %{_texmfdistdir}/doc/generic/bagpipe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
