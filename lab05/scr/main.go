package main

import (
	"fmt"
	"time"

	"github.com/brianvoe/gofakeit"
)

type Person struct {
	no          int
	startName   time.Time
	name        string
	startEmail  time.Time
	email       string
	startNumber time.Time
	phone       string
}

type Queue struct {
	q [](*Person)
	l int
}

func createQueue(amount int) *Queue {
	q := new(Queue)
	q.q = make([](*Person), amount, amount)
	q.l = -1

	return q
}

func (q *Queue) push(p *Person) {
	if q.l != len(q.q)-1 {
		q.q[q.l+1] = p
		q.l++
	}
}

func (q *Queue) pop() *Person {
	p := q.q[0]
	q.q = q.q[1:]
	q.l--

	return p
}

// var q *Queue
func Сonveyor(n int) *Queue {
	bread := make(chan *Person, 1)
	s := make(chan *Person, 1)
	t := make(chan *Person, 1)

	q := createQueue(n)
	for i := 1; i <= n; i++ {
		go produce(bread)
	}
	for i := 1; i <= n; i++ {
		go consume(bread, s)
	}
	for i := 1; i <= n; i++ {
		go ret(s, t)
	}
	for i := 1; i <= n; i++ {
		time.Sleep(100 * time.Microsecond)
		el := <-t
		q.push(el)
	}
	return q
}
func main() {
	n := 30
	q := Сonveyor(n)
	for i := 1; i <= n; i++ {
		el := q.pop()
		fmt.Println("The", i, "person:")
		fmt.Println(el.name, "|", el.email, "|", el.phone)
		fmt.Println(el.startEmail)
		fmt.Println(el.startName)
		fmt.Println(el.startNumber)
		fmt.Println()
	}
	// el := q.pop()
	// fmt.Println(el.name)

}

func produce(ch chan<- *Person) {
	var pers Person
	pers.email = gofakeit.Email()
	pers.startEmail = time.Now()
	ch <- (&pers)
}

func consume(ch chan *Person, ch1 chan *Person) {
	pers := <-ch
	pers.name = gofakeit.Name()
	pers.startName = time.Now()
	ch1 <- pers
}

func ret(ch chan *Person, ch1 chan *Person) {
	pers := <-ch
	pers.phone = gofakeit.Phone()
	pers.startNumber = time.Now()
	ch1 <- pers
	// q.push(pers)
}
