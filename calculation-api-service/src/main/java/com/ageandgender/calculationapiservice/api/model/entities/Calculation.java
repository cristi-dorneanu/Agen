package com.ageandgender.calculationapiservice.api.model.entities;

import com.ageandgender.calculationapiservice.api.model.enums.CalculationStatus;
import com.ageandgender.calculationapiservice.api.model.enums.CalculationType;
import com.ageandgender.calculationapiservice.api.model.enums.Gender;

import javax.persistence.*;

@Entity
public class Calculation {

    @Id
    @GeneratedValue
    private Long id;

    private CalculationStatus status;

    private CalculationType type;

    @Column(name = "estimated_gender")
    private Gender estimatedGender;

    @Column(name = "estimated_age")
    private Integer estimatedAge;

    @Column(name = "is_face")
    private boolean isFace;

    @Lob
    private String image;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public CalculationStatus getStatus() {
        return status;
    }

    public void setStatus(CalculationStatus status) {
        this.status = status;
    }

    public CalculationType getType() {
        return type;
    }

    public void setType(CalculationType type) {
        this.type = type;
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

    public boolean isFace() {
        return isFace;
    }

    public void setFace(boolean face) {
        isFace = face;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
}
