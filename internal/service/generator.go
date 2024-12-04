package service

import (
	"maze/internal/models"
)

func GenerateMaze(m models.MazeGenerator) ([][]rune, error) {
	maze, err := m.GenerateMaze()
	if err != nil {
		return nil, err
	}

	return maze, nil
}
