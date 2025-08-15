deps:
	scripts/deps/build-dependencies-mac.sh deps

config:
	cmake -Bbuild-release -DCMAKE_BUILD_TYPE=Release -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON -DCMAKE_PREFIX_PATH="$(PWD)/deps"

build:
	cmake --build build-release --parallel
