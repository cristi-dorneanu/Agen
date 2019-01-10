package com.ageandgender.calculationapiservice.api.model.dto;

import com.ageandgender.calculationapiservice.api.model.enums.CalculationType;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class Task implements Serializable {

    private Long calculationId;

    private CalculationType calculationType;

    private byte[] image;

    public Task() {
    }

    public Task(@JsonProperty("calculationId") Long calculationId,
                @JsonProperty("calculationId") CalculationType calculationType,
                @JsonProperty("calculationId") byte[] image) {
        this.calculationId = calculationId;
        this.calculationType = calculationType;
        this.image = image;
    }

    public Long getCalculationId() {
        return calculationId;
    }

    public void setCalculationId(Long calculationId) {
        this.calculationId = calculationId;
    }

    public CalculationType getCalculationType() {
        return calculationType;
    }

    public void setCalculationType(CalculationType calculationType) {
        this.calculationType = calculationType;
    }

    public byte[] getImage() {
        return image;
    }

    public void setImage(byte[] image) {
        this.image = image;
    }
}
