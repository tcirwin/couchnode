SOURCE = src/couchbase_impl.cc src/couchbase_impl.h src/args.cc src/notify.cc     \
         src/namemap.cc src/operations.cc src/namemap.h src/cas.cc      \
         src/cas.h

all: configure $(SOURCE)
	@node-gyp build

configure: $(bindings.gyp)
	@node-gyp configure

clean:
	@node-gyp clean

install:
	@node-gyp install

dist:
	@node-waf dist

remove:
	@node-gyp remove

check:
	(cd tests && ./runtests.sh 0*.js)

reformat:
	@astyle --mode=c \
               --quiet \
               --style=1tbs \
               --indent=spaces=4 \
               --indent-namespaces \
               --indent-col1-comments \
               --max-instatement-indent=78 \
               --pad-oper \
               --pad-header \
               --add-brackets \
               --unpad-paren \
               --align-pointer=name \
               src/*.cc \
               src/*.h
