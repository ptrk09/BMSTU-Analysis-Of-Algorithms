package main

import "testing"

func BenchmarkConveyor1(b *testing.B) {
	N := 1

	for i := 0; i < b.N; i++ {
		Сonveyor(N)

	}
}

func BenchmarkConveyor5(b *testing.B) {
	N := 5

	for i := 0; i < b.N; i++ {

		Сonveyor(N)

	}
}

func BenchmarkConveyor10(b *testing.B) {
	N := 10

	for i := 0; i < b.N; i++ {

		Сonveyor(N)

	}
}

func BenchmarkConveyor20(b *testing.B) {
	N := 20

	for i := 0; i < b.N; i++ {

		Сonveyor(N)

	}
}

func BenchmarkConveyor100(b *testing.B) {
	N := 100

	for i := 0; i < b.N; i++ {
		Сonveyor(N)
	}
}
