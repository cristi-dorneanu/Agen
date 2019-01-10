package com.ageandgender.calculationapiservice.api.repository;

import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CalculationRepository extends JpaRepository<Calculation, Long> {
}
