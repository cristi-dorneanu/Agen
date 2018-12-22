package com.ageandgender.calculationsearchservice.model.entities;

import com.ageandgender.calculationsearchservice.model.enums.Gender;

import javax.persistence.*;

@Entity
public class Calculation {

    @Id
    @GeneratedValue
    public Long id;

    @Column(name = "estimated_gender")
    public Gender estimatedGender;

    @Column(name = "estimated_age")
    public Integer estimatedAge;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Gender getEstimatedGender() {
        return estimatedGender;
    }

    public void setEstimatedGender(Gender estimatedGender) {
        this.estimatedGender = estimatedGender;
    }

    public Integer getEstimatedAge() {
        return estimatedAge;
    }

    public void setEstimatedAge(Integer estimatedAge) {
        this.estimatedAge = estimatedAge;
    }
}
