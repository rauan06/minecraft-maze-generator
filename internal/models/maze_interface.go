package models

import (
	"fmt"

	"math/rand"
)

// MazeGenerator is implemented by anu figure struct. It provides functionality
// to create maze, and create maze pattern to make it a maze.
type MazeGenerator interface {
	GenerateMaze() ([][]rune, error)
	GetLen() (length int)
	LengthDescriptionWord() (desc string)
	CreateGrid()
	GenerateMazePattern()
}

// Circle mazes
type Circle struct {
	Radius int
}

func (c *Circle) GetLen() (length int) { return c.Radius }

func (c *Circle) LengthDescriptionWord() (desc string) { return "radius" }

// TODO
func (c *Circle) GenerateMaze() ([][]rune, error) { return nil, nil }

func (c *Circle) CreateGrid() {}

func (c *Circle) GenerateMazePattern() {}

// Cube mazes
type Cube struct {
	Width int
	Grid  [][]rune
}

func (c *Cube) GetLen() (length int) { return c.Width }

func (c *Cube) LengthDescriptionWord() (desc string) { return "width" }

func (c *Cube) GenerateMaze() ([][]rune, error) {
	if err := checkLength(c); err != nil {
		return nil, err
	}

	c.CreateGrid()
	c.GenerateMazePattern()

	return c.Grid, nil
}

func (c *Cube) CreateGrid() {
	c.Grid = make([][]rune, c.Width)

	for i := range c.Grid {
		c.Grid[i] = make([]rune, c.Width)
	}
}

func (c *Cube) GenerateMazePattern() {
	startY, startX := rand.Intn(c.Width), rand.Intn(c.Width)

	endY, endX := rand.Intn(c.Width), rand.Intn(c.Width)
	for endY != startY && endX != startX {
		endY, endX = rand.Intn(c.Width), rand.Intn(c.Width)
	}

}

// Helper functions
func checkLength(m MazeGenerator) error {
	if m.GetLen() < 0 {
		return fmt.Errorf("%s cannot be negative", m.LengthDescriptionWord())
	}

	if m.GetLen() < 10 {
		return fmt.Errorf("%s should be at least 10", m.LengthDescriptionWord())
	}

	return nil
}
