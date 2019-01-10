package com.ageandgender.calculationapiservice.api.model.dto;

import com.ageandgender.calculationapiservice.api.model.enums.CalculationStatus;
import com.ageandgender.calculationapiservice.api.model.enums.Gender;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Arrays;

public class CalculationResult implements Serializable {

    private Long calculationId;

    private CalculationStatus calculationStatus;

    private Gender estimatedGender;

    private Integer estimatedAge;

    private boolean isFace;

    private byte[] image;

    public CalculationResult(@JsonProperty("calculationId") Long calculationId,
                             @JsonProperty("calculationStatus") CalculationStatus calculationStatus,
                             @JsonProperty("estimatedGender") Gender estimatedGender,
                             @JsonProperty("estimatedAge") Integer estimatedAge,
                             @JsonProperty("isFace") boolean isFace,
                             @JsonProperty("image") byte[] image) {
        this.calculationId = calculationId;
        this.calculationStatus = calculationStatus;
        this.estimatedGender = estimatedGender;
        this.estimatedAge = estimatedAge;
        this.isFace = isFace;
        this.image = image;
    }

    public Long getCalculationId() {
        return calculationId;
    }

    public void setCalculationId(Long calculationId) {
        this.calculationId = calculationId;
    }

    public CalculationStatus getCalculationStatus() {
        return calculationStatus;
    }

    public void setCalculationStatus(CalculationStatus calculationStatus) {
        this.calculationStatus = calculationStatus;
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

    public byte[] getImage() {
        return image;
    }

    public void setImage(byte[] image) {
        this.image = image;
    }

    @Override
    public String toString() {
        return "CalculationResult{" +
                "calculationId=" + calculationId +
                ", calculationStatus=" + calculationStatus +
                ", estimatedGender=" + estimatedGender +
                ", estimatedAge=" + estimatedAge +
                ", isFace=" + isFace +
                ", image=" + Arrays.toString(image) +
                '}';
    }
}
