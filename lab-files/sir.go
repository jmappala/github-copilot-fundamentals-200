package main

type SIRModel struct {
    TotalPopulation  float64
    InitialInfected  float64
    InitialRecovered float64
    Beta             float64
    Gamma            float64
}

func NewSIRModel(totalPopulation, initialInfected, initialRecovered, beta, gamma float64) *SIRModel {
    return &SIRModel{
        TotalPopulation:  totalPopulation,
        InitialInfected:  initialInfected,
        InitialRecovered: initialRecovered,
        Beta:             beta,
        Gamma:            gamma,
    }
}

func main() {
    // Create a new SIRModel
    model := NewSIRModel(1000, 1, 0, 0.5, 0.1)

    // Use the model
    // ...
}