%global tl_name bagpipe
%global tl_revision 34393

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.02
Release:	%{tl_revision}.1
Summary:	Support for typesetting bagpipe music
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/bagpipe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bagpipe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typesetting bagpipe music in MusixTeX is needlessly tedious. This
package provides specialized and re-defined macros to simplify this
task.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/bagpipe
%dir %{_datadir}/texmf-dist/tex/generic/bagpipe
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/BlackDonald.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/BlackDonald.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Bonnets.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Bonnets.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Green.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Green.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/GreenTwo.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/GreenTwo.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/README
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Washer.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/Washer.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/bagdoc.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/bagdoc.tex
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/quickref.pdf
%doc %{_datadir}/texmf-dist/doc/generic/bagpipe/quickref.tex
%{_datadir}/texmf-dist/tex/generic/bagpipe/bagpipe.ini
%{_datadir}/texmf-dist/tex/generic/bagpipe/bagpipe.tex
%{_datadir}/texmf-dist/tex/generic/bagpipe/bagpipex.ini
