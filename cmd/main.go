package main

import (
	"fmt"
	"maze/internal/models"
	"maze/internal/service"
)

func main() {
	obj := &models.Cube{Width: 10}

	maze, _ := service.GenerateMaze(obj)
	fmt.Println(maze)
}
