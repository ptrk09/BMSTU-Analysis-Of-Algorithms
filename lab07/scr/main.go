package main

// {"id":number, "Teamname": string}
// {"id":0, "Teamname": "PostavteZachotPls"}
import (
	"crypto/rand"
	"fmt"
	"reflect"
	"sort"

	"github.com/brianvoe/gofakeit"
	"github.com/logrusorgru/aurora"
)

func main() {
	fmt.Printf("%v", aurora.Magenta("Поиск в массиве словарей\n\n"))

	darr := CreateArray(10)
	farr := darr.FAnalysis()
	gt := "applicationpursue849"

	fmt.Printf("%v %v\n\n", aurora.Green("Ключ для поиска:"), aurora.Blue(gt))
	darr.Print()
	fmt.Println()

	r := farr.Combined(gt)
	if r["teamname"] == nil {
		fmt.Printf("%v\n", aurora.Red("Словарь с данным ключом не найден"))
	} else {
		fmt.Printf("%v\n", aurora.Green("Словарь с данным ключом найден"))
		r.Print()
	}
}

// CreateArray used to create DictArray with given size.
func CreateArray(n int) DictArray {
	var (
		darr DictArray
		g    Dict
	)

	darr = make(DictArray, n)

	for i := 0; i < n; i++ {
		dup := true
		for dup != false {
			g = Dict{
				"id":       gofakeit.Uint8(),
				"teamname": gofakeit.Teams(),
			}
			dup = g.IsDup(darr[:i])
		}

		darr[i] = g
	}

	return darr
}

// IsDup used to check whether Dict presents in given DictArray.
func (d Dict) IsDup(darr DictArray) bool {
	for _, v := range darr {
		if reflect.DeepEqual(d, v) {
			return true
		}
	}
	return false
}

// Print used to print single Dict.
func (d Dict) Print() {
	fmt.Printf("ID: %v\nTeamname: %v\n", d["id"], d["teamname"])
}

// Print used to print single DictArray.
func (darr DictArray) Print() {
	for _, d := range darr {
		d.Print()
	}
}

func (darr DictArray) Pick(l string) string {
	for _, d := range darr {
		if d["teamname"].(string)[:1] == l {
			return d["teamname"].(string)
		}
	}

	i := rand.Int() % len(darr)

	return darr[i]["teamname"].(string)
}

// Brute used to find value using bruteforce method.
func (darr DictArray) Brute(gt string) Dict {
	var r Dict

	for _, d := range darr {
		if d["teamname"] == gt {
			return d
		}
	}

	return r
}

// Binary used to find value using binary search method.
func (darr DictArray) Binary(gt string) Dict {
	var (
		l   int = len(darr)
		mid int = l / 2
		r   Dict
	)

	switch {
	case l == 0:
		return r
	case darr[mid]["teamname"].(string) > gt:
		r = darr[:mid].Binary(gt)
	case darr[mid]["teamname"].(string) < gt:
		r = darr[mid+1:].Binary(gt)
	default:
		r = darr[mid]
	}

	return r
}

// FAnalysis used to analyse frequency of given DictArray.
func (darr DictArray) FAnalysis() FreqArray {
	var (
		az   string    = "abcdefghijklmnopqrstuvwxyz"
		farr FreqArray = make(FreqArray, len(az))
	)

	for i, v := range az {
		a := Freq{
			l:    string(v),
			cnt:  0,
			darr: make(DictArray, 0),
		}
		farr[i] = a
	}

	for _, v := range darr {
		l := v["teamname"].(string)[:1]
		for i := range farr {
			if farr[i].l == l {
				farr[i].cnt++
			}
		}
	}

	sort.Slice(farr, func(i, j int) bool {
		return farr[i].cnt > farr[j].cnt
	})

	for i := range farr {
		for j := range darr {
			if darr[j]["teamname"].(string)[:1] == farr[i].l {
				farr[i].darr = append(farr[i].darr, darr[j])
			}
		}

		sort.Slice(farr[i].darr, func(l, m int) bool {
			return farr[i].darr[l]["teamname"].(string) < farr[i].darr[m]["teamname"].(string)
		})
	}

	return farr
}

// Combined used to find value using binary search and frequency analysis method.
func (farr FreqArray) Combined(w string) Dict {
	var (
		l string = w[:1]
		r Dict
	)

	for _, d := range farr {
		if string(d.l) == l {
			r = d.darr.Binary(w)
		}
	}

	return r
}

// Dict used to represent dictionary with custom types.
type Dict map[string]interface{}

// DictArray used to represent array of Dict instances.
type DictArray []Dict

// Freq used to represent frequency analyser type.
type Freq struct {
	l    string
	cnt  int
	darr DictArray
}

// FreqArray used to represent array of Freq instances.
type FreqArray []Freq
