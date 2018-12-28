package com.ageandgender.calculationsearchservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@EnableDiscoveryClient
@SpringBootApplication
public class CalculationSearchServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(CalculationSearchServiceApplication.class, args);
	}

}

