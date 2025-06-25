package com.warmhouse.devicemanagement;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;

@RestController
public class DeviceController {

    public static class NewDeviceRequest {
        public String name;
        public String desc;
        public int houseID;
        public int deviceTypeID;
    }

    public static class Device {
        public int id;
        public String name;
        public String desc;
        public int houseID;
        public int deviceTypeID;
        public String registrationTime;
    }

    @PostMapping("/devices")
    @ResponseStatus(HttpStatus.CREATED)
    public Device registerDevice(@RequestBody NewDeviceRequest req) {
        Device device = new Device();
        device.id = 1;
        device.name = req.name;
        device.desc = req.desc;
        device.houseID = req.houseID;
        device.deviceTypeID = req.deviceTypeID;
        device.registrationTime = LocalDate.now().toString();
        return device;
    }
}