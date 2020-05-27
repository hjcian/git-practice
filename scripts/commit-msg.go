package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func readCommitMsg(fpath string) string {
	content, err := ioutil.ReadFile(fpath)
	if err != nil {
		log.Fatal(err)
	}
	return string(content)
}

func main() {
	args := os.Args
	fmt.Println("===== Start =====")
	fmt.Println("Arg:", args)
	msg := readCommitMsg(args[1])
	fmt.Println("Msg:", msg)
	fmt.Println("=====  End  =====")
}
